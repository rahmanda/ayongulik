def main(formal, rsvp, number_of_friends, gift_price, almamater):
    if formal == True and rsvp == True:
        if number_of_friends <= 2 and gift_price >= 200:
            print('Diterima')
        elif (number_of_friends <= 2 or gift_price >= 200) and (almamater == "Unpar" or almamater == "UHasselt"):
            print('Diterima')
        else:
            print('Ditolak')
    else:
        print('Ditolak')


if __name__ == '__main__':
    # Test case 1
    main(True, True, 2, 200, 'UHasselt')
    # Test case 2
    main(True, True, 2, 200, 'BSI')
    # Test case 3
    main(True, True, 2, 100, 'Unpar')
    # Test case 4
    main(True, False, 2, 200, 'Unpar')
    # Test case 5
    main(True, True, 5, 200, 'Unpar')