using System;
using System.Threading;

namespace AlgorithmicToolBox
{
    class Program
    {
        static void Main()
        {
            long count = long.Parse(Console.ReadLine());


            if (count != 0)
            {
                var arrFibo = new long[count + 1];
                long newM = (count + 2) % 60;
                long new_last = FibonacciLastDigit(arrFibo, newM);
                if (new_last == 0) Console.WriteLine(9);
                else
                {
                    Console.WriteLine(-1);
                }
            }
            else
            {
                Console.WriteLine(count);

            }
        }



        public static long FibonacciLastDigit(long[] arrFib, long count)
        {
            arrFib[0] = 0;
            arrFib[1] = 1;

            for (long i = 2; i < arrFib.Length; i++)
            {

                arrFib[i] = (arrFib[i - 1] % 10 + arrFib[i - 2] % 10) % 10;

            }
            return arrFib[arrFib.Length - 1];

        }
    }
}