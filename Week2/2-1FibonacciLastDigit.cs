using System;

namespace AlgorithmicToolBox
{
    class Program
    {
        static void Main()
        {
            long count = long.Parse(Console.ReadLine());
            long fib;

            if (count != 0)
            {
                var arrFibo = new long[count + 1];
                fib = Fibonacci(arrFibo, count + 1);

                Console.WriteLine(fib);
            }
            else
            {
                Console.WriteLine(count);

            }
        }

        public static long Fibonacci(long[] arrFib, long count)
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