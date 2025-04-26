import io
import os

def last_lines(file_path, bufsize=io.DEFAULT_BUFFER_SIZE):
    try:
        with open(file_path, 'rb') as f:
            f.seek(0, os.SEEK_END)
            pos = f.tell()
            buffer = b''
            first_pass = True

            while pos > 0:

                read_size = min(bufsize, pos)
                pos -= read_size
                f.seek(pos)
                chunk = f.read(read_size)


                buffer = chunk + buffer


                parts = buffer.split(b'\n')

                if first_pass and pos == 0 and parts and parts[-1] == b'':
                    parts = parts[:-1]

                first_pass = False


                buffer = parts[0]

                for segment in reversed(parts[1:]):

                    cleaned = segment.rstrip(b'\r')
                    yield cleaned.decode('utf-8') + '\n'

            if buffer:
                cleaned = buffer.rstrip(b'\r')
                yield cleaned.decode('utf-8') + '\n'
                
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except PermissionError:
        print(f"Erro: Permissão negada para acessar o arquivo '{file_path}'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        
        
        
#----------------------------------------------------------------------------------------------------------

# cria o arquivo de teste
with open('my_file.txt', 'w', encoding='utf-8') as f:
    f.write("This is a file\n")
    f.write("This is line 2\n")
    f.write("And this is line 3\n")
    
    
#--------------------------------------------------------------------------------------------------------------

for line in last_lines('my_file.txt'):
    print(line, end='')
    
    
lines = last_lines('my_file.txt')
next(lines)
next(lines)
next(lines)