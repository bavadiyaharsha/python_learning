"""
Enter 'a' to add movies, 'l' to add see your movie, 'f' to find movie and 'q' to quit movie


-Add movie
-see movies
-find movies 
-stop running the program

Task:
1. Decide where to strore movie
2.what is the foramte of movie?
3. shoow the user main interface and get their input
4. allowed user to add movie
5. show all their movie
6. find movie
7.stop running program when they type 'q'


"""

movies=[]

def manu():
    user_input=input("Enter 'a' to add movies, 'l' to add see your movie, 'f' to find movie and 'q' to quit movie: ")     
    while user_input!='q':
        if user_input=='a':
            add_movie()  
        elif user_input=='l':
            show_movies()
        elif user_input=='f':
            find_movie()
        else:
            print("Unknown - commmand execute try again....")                                                                                           
                                                                                                     
        user_input=input("Enter 'a' to add movies, 'l' to add see your movie, 'f' to find movie and 'q' to quit movie: ")
    
  
  
def add_movie():
    name=input("enter the Name of movie:")
    director= input("enter the Name of Director:")
    year=int(input("enter the Year:"))
    movies.append({
        'name':name,
        'director':director,
        'year':year})
    
  
    
def show_movies():
   for movie in movies:
    print(f"Name :{movie['name']}")
    print(f"Director :{movie['director']}")
    print(f"Year :{movie['year']}")



def show_movie_detail():
    print(f"Name :{movies['name']}")
    print(f"Director :{movies['director']}")
    print(f"Year :{movies['year']}")


manu()



         
             
         
     
            
