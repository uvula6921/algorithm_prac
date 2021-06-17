genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays = [2000, 500, 600, 150, 800, 2500, 2000]

def get_melon_best_album(genre_array, play_array):
  sum_dict = {}
  music_dict = {}
  result = []
  for i in range(len(genre_array)):
    if genre_array[i] not in sum_dict:
      sum_dict[genre_array[i]] = play_array[i]
      music_dict[genre_array[i]] = [[i, play_array[i]]]
    else:
      sum_dict[genre_array[i]] += play_array[i]
      music_dict[genre_array[i]].append([i, play_array[i]])
    
  sum_dict = sorted(sum_dict, key= lambda x : sum_dict[x], reverse=True)
  for i in sum_dict:
    music_dict[i] = sorted(music_dict[i], key=lambda x:x[1], reverse=True)
    for j in range(len(music_dict[i])):
      if j > 1:
        break
      result.append(music_dict[i][j][0])
    
    
  return result

print(get_melon_best_album(genres, plays))