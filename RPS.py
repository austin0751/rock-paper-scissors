def player(prev_play, opponent_history=[], pattern_length=3):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < pattern_length:
        # Play randomly while collecting enough history
        return "R" if len(opponent_history) % 3 == 0 else ("P" if len(opponent_history) % 3 == 1 else "S")

    # Look for patterns in the opponent's play history
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

    # Predict the next move based on the most common follow-up move to the last sequence
    next_moves = pattern_count.get(last_sequence, {})
    if next_moves:
        prediction = max(next_moves, key=next_moves.get)
        # Counter the predicted move
        if prediction == "R":
            return "P"
        elif prediction == "P":
            return "S"
        else:
            return "R"
    else:
        # Default to rock if no pattern is detected
        return "R"
