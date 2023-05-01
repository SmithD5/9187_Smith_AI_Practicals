def get_valid_moves(state):
    
    top_disks=[peg[-1] if peg else float('inf') for peg in state]
    valid_moves=[]
    
    for i in range(len(state)):
        for j in range(len(state)):
            if i!=j:
                if top_disks[i]<top_disks[j]:
                    valid_moves.append((i,j))
                    
    return valid_moves
    
def apply_moves(state,moves):
    
    src,dst=moves
    
    src_list, dst_list= list(state[src]), list(state[dst])
    
    dst_list.append(src_list.pop())
    
    new_state=list(state)
    new_state[src]=tuple(src_list)
    new_state[dst]=tuple(dst_list)
    
    return tuple(new_state)
    

def bfs(n):
    starting_state=(tuple(i for i in range(n, 0,-1)),(),())
    goal_state=((),(),tuple(i for i in range(n, 0,-1)))
    
    queue=[]
    queue.append(starting_state)
    visited=set()
    parents={}
    
    while queue:
        
        current_state=queue.pop(0)
        
        if current_state== goal_state:
            
            store=[]
            
            while current_state != starting_state:
                store.append(current_state)
                current_state=parents[current_state]
            
            store.append(current_state)
            store.reverse()
            return store
        
        visited.add(current_state)
        valid_moves=get_valid_moves(current_state)
        
        for i in valid_moves:
            next_state=apply_moves(current_state,i)
            
            
            if next_state not in visited:
                queue.append(next_state)
                parents[next_state]=current_state
    return None
    
n=5
optimal_solution=bfs(n)
if optimal_solution:
    for i in optimal_solution:
        print(i)
else:
    print(f"No Optimal Solution found for {n} disks")