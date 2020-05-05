using System;


namespace LCM
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            var cookies = input.Split(' ');
            var num1 = long.Parse(cookies[0]);
            var num2 = long.Parse(cookies[1]);

            var lcm = num1 * num2 / GCD(num1, num2);
            Console.WriteLine(lcm);
        }
        public static long GCD(long a, long b)
        {
            if (b == 0) return a;

            long reminder = a % b;

            return GCD(b, reminder);
        }
    }
}