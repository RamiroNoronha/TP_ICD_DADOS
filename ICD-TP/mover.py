import os
out = open('/home/artixs/Documents/Downloads/covid19br-vac-main/covid19br-vac-main/tudo.csv', 'w')
for file in os.listdir('/home/artixs/Documents/Downloads/covid19br-vac-main/covid19br-vac-main/processed'):
    f = open(f'/home/artixs/Documents/Downloads/covid19br-vac-main/covid19br-vac-main/processed/{file}')
    print(file)
    next(f)
    for line in f:
        out.write(line)

    f.close()

out.close()