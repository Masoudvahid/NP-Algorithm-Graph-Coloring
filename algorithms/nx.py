from algorithms.headers import *

def equitable_color(G, num_colors):
    """Provides equitable (r + 1)-coloring for nodes of G in O(r * n^2) time
    if deg(G) <= r. The algorithm is described in [1]_.

    Attempts to color a graph using r colors, where no neighbors of a node
    can have same color as the node itself and the number of nodes with each
    color differ by at most 1.

    Parameters
    ----------
    G : networkX graph
       The nodes of this graph will be colored.

    num_colors : number of colors to use
       This number must be at least one more than the maximum degree of nodes
       in the graph.

    Returns
    -------
    A dictionary with keys representing nodes and values representing
    corresponding coloring.

    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> d = nx.coloring.equitable_color(G, num_colors=3)
    >>> nx.algorithms.coloring.equitable_coloring.is_equitable(G, d)
    True

    Raises
    ------
    NetworkXAlgorithmError
        If the maximum degree of the graph ``G`` is greater than
        ``num_colors``.

    References
    ----------
    .. [1] Kierstead, H. A., Kostochka, A. V., Mydlarz, M., & Szemerédi, E.
        (2010). A fast algorithm for equitable coloring. Combinatorica, 30(2),
        217-224.
    """

    # Map nodes to integers for simplicity later.
    nodes_to_int = {}
    int_to_nodes = {}

    for idx, node in enumerate(G.nodes):
        nodes_to_int[node] = idx
        int_to_nodes[idx] = node

    G = nx.relabel_nodes(G, nodes_to_int, copy=True)

    # Basic graph statistics and sanity check.
    if len(G.nodes) > 0:
        r_ = max([G.degree(node) for node in G.nodes])
    else:
        r_ = 0

    if r_ >= num_colors:
        raise nx.NetworkXAlgorithmError(
            f"Graph has maximum degree {r_}, needs "
            f"{r_ + 1} (> {num_colors}) colors for guaranteed coloring."
        )

    # Ensure that the number of nodes in G is a multiple of (r + 1)
    pad_graph(G, num_colors)

    # Starting the algorithm.
    # L = {node: list(G.neighbors(node)) for node in G.nodes}
    L_ = {node: [] for node in G.nodes}

    # Arbitrary equitable allocation of colors to nodes.
    F = {node: idx % num_colors for idx, node in enumerate(G.nodes)}

    C = make_C_from_F(F)

    # The neighborhood is empty initially.
    N = make_N_from_L_C(L_, C)

    # Currently all nodes witness all edges.
    H = make_H_from_C_N(C, N)

    # Start of algorithm.
    edges_seen = set()

    for u in sorted(G.nodes):
        for v in sorted(G.neighbors(u)):

            # Do not double count edges if (v, u) has already been seen.
            if (v, u) in edges_seen:
                continue

            edges_seen.add((u, v))

            L_[u].append(v)
            L_[v].append(u)

            N[(u, F[v])] += 1
            N[(v, F[u])] += 1

            if F[u] != F[v]:
                # Were 'u' and 'v' witnesses for F[u] -> F[v] or F[v] -> F[u]?
                if N[(u, F[v])] == 1:
                    H[F[u], F[v]] -= 1  # u cannot witness an edge between F[u], F[v]

                if N[(v, F[u])] == 1:
                    H[F[v], F[u]] -= 1  # v cannot witness an edge between F[v], F[u]

        if N[(u, F[u])] != 0:
            # Find the first color where 'u' does not have any neighbors.
            Y = [k for k in C.keys() if N[(u, k)] == 0][0]
            X = F[u]
            change_color(u, X, Y, N=N, H=H, F=F, C=C, L=L_)

            # Procedure P
            procedure_P(V_minus=X, V_plus=Y, N=N, H=H, F=F, C=C, L=L_)

    return {int_to_nodes[x]: F[x] for x in int_to_nodes}
