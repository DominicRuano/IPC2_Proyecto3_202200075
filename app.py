# Importaciones
import os
import threading

# Levantar backend
def StartBackEnd():
    os.system("python back/back.py")

# Levantar backend
def StartFrontEnd():
    os.system("python front/manage.py runserver")

# Corriendo
thread1 = threading.Thread(target=StartBackEnd)
thread2 = threading.Thread(target=StartFrontEnd)

# Inicia los hilos
thread1.start()
thread2.start()

# Espera a que ambos hilos terminen
thread1.join()
thread2.join()


