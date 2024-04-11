def player(prev_play, opponent_history=[], pattern_length=3):
    if prev_play:
        opponent_history.append(prev_play)

    # If history is not long enough, play randomly
    if len(opponent_history) < pattern_length:
        return "R" if len(opponent_history) % 3 == 0 else ("P" if len(opponent_history) % 3 == 1 else "S")

    # Look for patterns in opponent's history
    last_sequence = "".join(opponent_history[-pattern_length:])
    pattern_count = {}

    # Analyze history for patterns
    for i in range(len(opponent_history) - pattern_length):
        seq = "".join(opponent_history[i:i + pattern_length])
        next_move = opponent_history[i + pattern_length]
        if seq in pattern_count:
            if next_move in pattern_count[seq]:
                pattern_count[seq][next_move] += 1
            else:
                pattern_count[seq][next_move] = 1
        else:
            pattern_count[seq] = {next_move: 1}

    # Predict opponent's next move based on pattern analysis
    last_sequence = "".join(opponent_history[-pattern_length:])
    next_moves = pattern_count.get(last_sequence, {})
    if next_moves:
        prediction = max(next_moves, key=next_moves.get)
        if prediction == "R":
            return "P"
        elif prediction == "P":
            return "S"
        else:
            return "R"
    else:
        # If no pattern is detected, play based on opponent's most frequent move
        most_frequent_move = max(opponent_history, key=opponent_history.count)
        if most_frequent_move == "R":
            return "P"
        elif most_frequent_move == "P":
            return "S"
        else:
            return "R"
