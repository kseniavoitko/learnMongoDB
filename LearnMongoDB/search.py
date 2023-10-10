from models import Authors, Qoutes

if __name__ == '__main__':
    while True:
        field, value = input('Give me comand field:value\n').split(':')
        # if field == 'name':
            # qoutes = Qoutes.objects(author__fullname=value)
            # for qoute in qoutes:
            #     print(qoute.to_mongo().to_dict())
        if field == 'tag':
            qoutes = Qoutes.objects(tags=value)
            for qoute in qoutes:
                print(qoute.to_mongo().to_dict())

