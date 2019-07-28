def movie_time(duration):
    hour = duration // 60
    #minute = duration - hour * 60
    minute = duration % 60
    return hour, minute

a, b = movie_time(int(input("Enter duration of movie in minutes: ")))
print(f" the movie is {a} hours {b} min long")
