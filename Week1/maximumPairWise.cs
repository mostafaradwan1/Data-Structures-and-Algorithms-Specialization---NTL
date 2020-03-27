using System;

namespace maximumPairwiseProduct
{
    class Program
    {
        static void Main()
        {

            var count = int.Parse(Console.ReadLine());
            var input = Console.ReadLine().Split();

            if (input != null)
            {
                var inputLength = input.Length;
                var numbers = new long[inputLength];
                long max = 0;
                long seMax = 0;

                for (int i = 0; i < inputLength; i++)
                {
                    numbers[i] = int.Parse(input[i]);
                }
            

                for (int i = 0; i < inputLength; i++)
                {
                
                    if (numbers[i]>max)
                    {
                        seMax = max;
                        max = numbers[i];
                    }

                    else if (seMax<numbers[i] )
                    {
                        seMax = numbers[i];
                    }

                }
                Console.WriteLine(max*seMax);
            }


            Console.ReadKey();
        }
    }
}
