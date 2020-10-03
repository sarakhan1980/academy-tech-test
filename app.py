from mycsv import csvparser


def main():
    try:
        file = open('./data/people-list.csv', 'r')

        while True:
            row = csvparser.read_row(file)

            if row is None:
                print("End of file reached")
                break

            print(row[0] + " - " + row[1] + " - " + row[2] + " - " + row[3])
    except Exception as e:
        print("Error reading CSV file - " + str(e))
        exit(1)
    finally:
        file.close()


if __name__ == '__main__':
    main()
