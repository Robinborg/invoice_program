
def quit_loop(close_loop:str)->bool:
    """For closing loops"""
    if close_loop.lower() == 'q' or close_loop.lower() == "quit":
        return True
    else:
        return False
            
