import os
from PIL import Image


#DIRECTORIOS DE ENTRADA Y SALIDA
input_dirs = ['train','test','validation']
base_input = './'
base_output = './comprimidos'

#PARAMETROS PARA REDIMENSIONAMIENTO
size = (128,128)
output_ext = '.jpeg'

#CREAMOS ESTRUCUTRA DE CARPETAS EN DIRECTORIO DE SALIDA
for dir_name in input_dirs:
    for subfolder in ['NORMAL','PNEUMONIA']:
        out_path = os.path.join(base_output,dir_name,subfolder)
        os.makedirs(out_path,exist_ok=True)

#PROCESAR IMAGENES
for dir_name in input_dirs:
    for subfolder in ['NORMAL','PNEUMONIA']:
        input_path = os.path.join(base_input,dir_name,subfolder)
        output_path = os.path.join(base_output,dir_name,subfolder)
        print(f'input path : {input_path}')
        print(f'output path : {output_path}')
        if not os.path.exists(input_path):
            continue
        for filename in os.listdir(input_path):
            file_path = os.path.join(input_path,filename)
            if not os.path.isfile(file_path):
                continue
            
            try:
                with Image.open(file_path) as img:
                    #img = img.convert('RGB')
                    img = img.resize(size,Image.LANCZOS)
                    output_file = os.path.splitext(filename)[0] + output_ext
                    output_file_path = os.path.join(output_path,output_file)
                    img.save(output_file_path,'JPEG',quality=85)
                    print(f'Imagen comprimida : {output_file_path}')
            except Exception as e:
                print(f'Error procesando imagenes {file_path} : {e}')
        