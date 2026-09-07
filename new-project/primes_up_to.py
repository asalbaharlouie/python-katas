def primes_up_to(n):
    primes_number= []
    for number in range(2, n):
        '''
        n میره روی تک‌تک اعداد از 2 تا  
        .(این‌ها کاندیدهای "شاید اول باشن")
        '''
        find_divisor = False
        for divisor in range(2, number-1):
            '''
            برای همون یه عدد فعلی که حلقه اول روش وایساده، میره روی تک‌تک مقسوم‌علیه‌های احتمالی (2 تا 1-عدد) 
            .و چک می‌کنه آیا عدد فعلی به هیچ‌کدوم از اون‌ها بخش‌پذیره یا نه
            '''
            if number % divisor == 0:
                find_divisor = True
        if find_divisor == False:
            primes_number.append(number)

    return primes_number

print(primes_up_to(20))