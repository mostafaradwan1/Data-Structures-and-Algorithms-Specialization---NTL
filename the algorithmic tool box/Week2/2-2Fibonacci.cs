using System;
using System.Threading;

namespace AlgorithmicToolBox
{
    class Program
    {
        static void Main()
        {
            int count = int.Parse(Console.ReadLine());


            long fib;
            if (count == 0)
                fib = 0;
            else
            {
                var arrFibo = new long[count + 1];
                fib = Fibonacci(arrFibo, count + 1);
            }
            Console.WriteLine(fib);



        }

        public static long Fibonacci(long[] arrFib, int count)
        {

            arrFib[0] = 0;
            arrFib[1] = 1;
            for (int i = 2; i < arrFib.Length; i++)
            {
                arrFib[i] = arrFib[i - 1] + arrFib[i - 2];

            }
            return arrFib[arrFib.Length - 1];

        }
    }
}