def load(root, player, enemy):
    player_x = player.winfo_x()
    player_y = player.winfo_y()
    player_size = int(player.cget("font").split()[1])  # extract the font size

    enemy_x = enemy.winfo_x()
    enemy_y = enemy.winfo_y()
    enemy_size = int(enemy.cget("font").split()[1])

    collision_x = (player_x + player_size >= enemy_x) and (player_x <= enemy_x + enemy_size)

    collision_y = (player_y + player_size >= enemy_y) and (player_y <= enemy_y + enemy_size)

    if collision_x and collision_y:
        from __main__ import game_running
        game_running = False
        root.after(0, root.destroy)

