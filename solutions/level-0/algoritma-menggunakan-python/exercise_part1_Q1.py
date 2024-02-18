def main(score, tolerable):
    if score >= 10:
        print('Lulus!')
    elif 9 <= score < 10 and tolerable:
        print('Lulus!')
    else:
        print('Tidak lulus~') 


if __name__ == '__main__':
    # Test case 1
    main(10, False)
    # Test case 2
    main(9, False)
    # Test case 3
    main(9, True)