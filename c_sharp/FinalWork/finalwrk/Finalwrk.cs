int count = 0;

int countLess(string[] input, int n) 
{
    for(int i = 0; i < input.Length; i++) 
    {
        if(input[i].Length <= n) 
        {
            count++;
        }
    }
    return count;
}

string[] findLess(string[] input, int n) 
{
    string[] output = new string[countLess(input, n)];
    for(int i = 0, j = 0; i < input.Length; i++) 
    {
        if(input[i].Length <= n) 
        {
            output[j] = input[i];
            j++;
        }
    }
    return output;
}

string[] Array() 
{
    Console.Write("Введите значения через пробел: ");
    return Console.ReadLine().Split(" ");
}

string[] array = Array();
string[] result = findLess(array, 3);
Console.WriteLine($"[{string.Join(", ", array)}] \n|\nv \n[{string.Join(", ", result)}]");