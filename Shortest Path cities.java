class Shortest{     //Shortest Path Between the cities
   
   int ShortestPath(int x, int y)
   {
       int res = 0;
       while (x != y)
       {
           if(x > y)
           x/=2;
           else
           y/=2;
           
           res++;
       }
       
       return res;
   }
}


           
