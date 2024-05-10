def expected_minimax(state, depth,  piece, maximizingPlayer  , tree  ):
    global NODE_EXPANDED
    NODE_EXPANDED += 1
	
    column_value = {}
	column_value_minimizing ={}

	valid_locations = get_valid_locations(state)
	is_terminal = is_terminal(state)

	if depth == 0 or is_terminal:
		return score_position(state, piece )

	if maximizingPlayer:
		value = -math.inf
		children = []
		for col in valid_locations:
			row = get_next_open_row(state, col)
			b_copy = state.copy()
			drop_piece(b_copy, row, col, AI_PIECE)
			node = Node(col, [], 0 , b_copy  )  # Set parent based on current depth

			returned_node , val  = expect_minimax(b_copy, depth - 1,  False, current_depth + 1 , node ,  piece % 2 + 1 ) 
			column_value[col] = val
		#   print("1")
			node.utility_value = val
		#   print(node.utility_value)
		#   print(node.board)
			tree.children.append(node)
			children.append(node)
			value = max(value, val)
			if value == val:  # Update best child if value has improved
				best_child = node

	# No need to set root.children here, children are appended within the loop
			#  0 1 2 4  -->  10 12 14 16
		max_value =  - math.inf 
		best_col = 0  
		#  column_value.keys() index out of bunds problem
#   1 2 5 6
		l = len(column_value_minimizing)
		i = 0 
		for    (col ,value) in column_value.items() :
      		# i += 1
        #     12356
			if column_value.get(col-1 , 0 )   ==  0 : 
				val = (0.6 * value) + (0.4 * column_value.get(col+1 , 0 ))
				if val > max_value : 
					max_value  = val  
					best_col = col
			elif column_value.get(col + 1 , 0 )   ==  0 : 
				val = (0.6 * value) + (0.4 * column_value.get(col-1 , 0 ))
				if val > max_value : 
					max_value  = val  
					best_col = col
			else : 
				val = (0.6 * value) + (0.2 * column_value.get(col-1 , 0 )  ) + (0.2 * column_value.get(col+1 , 0 ))
				if val > max_value : 
					max_value  = val  
					best_col = col
				
    
	else:  # Minimizing player
		value = math.inf
		children = []
		for col in valid_locations:
			row = get_next_open_row(state, col)
			b_copy = state.copy()
			drop_piece(b_copy, row, col, PLAYER_PIECE)
			node = Node(col, [], 0 , b_copy  )  # Set parent based on current depth

			returned_node , val = expect_minimax(b_copy, depth - 1,  True, current_depth + 1 , node  ,  piece % 2 + 1)
			column_value_minimizing[col] = val

			#   node = Node(col, returned_node.children, returned_node.utility_value, b_copy, parent=root if current_depth == 0 else root.children[current_depth - 1])  # Set parent based on current depth
			children.append(node)
			node.utility_value = val
			tree.children.append(node)
			value = min(value, val)
			if value == val: 
				best_child = node

		max_value =  math.inf 
		for    (col ,value) in column_value_minimizing.items() :

			if column_value_minimizing.get(col-1 , 0 )   ==  0 : 
				val = (0.6 * value) + (0.4 * column_value_minimizing.get(col+1 , 0 ))
				if val < max_value : 
					max_value  = val  
			elif column_value_minimizing.get(col + 1 , 0 )   ==  0 : 
				val = (0.6 * value) + (0.4 * column_value_minimizing.get(col-1 , 0 ))
				if val < max_value : 
					max_value  = val  
			else : 
				val = (0.6 * value) + (0.2 * column_value_minimizing.get(col-1 , 0 )  ) + (0.2 * column_value_minimizing.get(col+1 , 0 ))
				if val < max_value : 
					max_value  = val  
					

	return   max_value