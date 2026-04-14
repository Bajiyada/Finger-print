def match_fingerprints(features1, features2):
    # Implement a simple matching algorithm based on Euclidean distance
    from scipy.spatial import distance

    if len(features1) == 0 or len(features2) == 0:
        return 0.0

    # Calculate the Euclidean distance between the two feature sets
    dist = distance.euclidean(features1, features2)

    # Convert distance to a similarity score (lower distance means higher similarity)
    similarity_score = 1 / (1 + dist)

    return similarity_score