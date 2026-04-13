def relax_edge(total_distances, node_a, node_b, dist_a_b):
    curr_b_dist = total_distances[node_b]
    curr_a_dist = total_distances[node_a]
    if (curr_a_dist + dist_a_b) < curr_b_dist:
        total_distances[node_b] = curr_a_dist + dist_a_b
        return True
    return False
