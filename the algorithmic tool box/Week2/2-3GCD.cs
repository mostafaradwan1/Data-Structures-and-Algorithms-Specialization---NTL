using System;

namespace maximumPairwiseProduct
{
    class Program
    {
        static void Main()
        {
            var input = Console.ReadLine();
            var cookies = input.Split(' ');
            var num1 = long.Parse(cookies[0]);
            var num2 = long.Parse(cookies[1]);

            Console.WriteLine(GCD(num1, num2));


        }

        public static long GCD(long a, long b)
        {
            if (b == 0) return a;

            long reminder = a % b;

            return GCD(b, reminder);
        }

    }
}