from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
# BaseModel crea el constructor y se puede pasar los parametros del objeto
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

user_list = [User(id=1,name="Fredo", surname= "Noriega", url= "arlequindev.com", age= 29),
         User(id=2,name="Ase", surname= "Mendieta", url= "kamaham.com", age= 30),
         User(id=3,name="Zuka", surname= "Anguiano", url= "zuka.com", age= 30)]

@app.get('/users')
async def usersjson(): 
    return user_list

@app.get('/usersclass')
async def usersclass():
    return user_list


# Path
@app.get('/user/{id}')
async def user(id: int):
    return search_user(id)
# Query     
@app.get('/user/')
async def user(id: int):
  return search_user(id)

# Post
@app.post('/user/')
async def user(user: User):
  if type(search_user(user.id)) == User: 
    return {"error": "El usuario ya existe"}
  else:
    user_list.append(user)
  return user
    
# Put
@app.put('/user/')
async def user(user: User):
  found = False
  for index,  saved_user in enumerate(user_list):
    if saved_user.id == user.id:
      user_list[index] = user 
      found = True
  if not found:
    return {"error": "No se ha actualizado el usuario"}    
  return user

# Delete
@app.delete('/user/{id}')
async def user(id: int):
  found = False
  for index,  saved_user in enumerate(user_list):
    if saved_user.id == id:
      del user_list[index]
      found = True
  if not found:
    return {"error": "No se ha eliminado el usuario"}
  

    

# helper
def search_user(id: int):
  users = filter(lambda user: user.id == id, user_list)
  try:
    return list(users)[0]
  except:
    return {"error": "No se ha encontraro el usuario"}    
  
  

      
        