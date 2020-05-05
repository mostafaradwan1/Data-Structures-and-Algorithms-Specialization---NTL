using System;

namespace AlgorithmicToolBox
{
    class Program
    {
        static void Main()
        {
            int count = 0;
            int money = int.Parse(Console.ReadLine());
            int mm = money / 10;
            count += mm;
            int ss = (money - (mm * 10)) / 5;
            count += ss;
            int ii = (money - ((mm * 10) + (ss * 5)));
            count += ii;
            Console.WriteLine(count);

        }

        public static int Change(int money)
        {
            int numOfCoins = 0;
            while (money > 0)
            {
                if (money >= 10)
                    money -= 10;
                else if (money >= 5)
                    money -= 5;
                else
                    money -= 1;
                numOfCoins += 1;
            }

            return numOfCoins;
        }




    }
}