using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace ConsoleApp1
{
  class Program
  {
    static Queue<Process> Proc = new Queue<Process>();
    static int pnum = 3;
    static Process[] p = new Process[pnum];


    static void Prior_Seter()
    {
        p[i].PriorityClass = ProcessPriorityClass.RealTime;
        p[i+2].PriorityClass = ProcessPriorityClass.Normal;
        p[i+4].PriorityClass = ProcessPriorityClass.Idle;
      
    }


    static void Main(string[] args)
    { 
      
      for (int i = 0; i <pnum; i++)
      {
        p[i] = new Process();
        p[i].StartInfo.FileName = "C:\\Windows\\system32\\mspaint.exe";
        p[i].Start();
        Proc.Enqueue(p[i]);
      }
      Prior_Seter();








      Console.ReadKey();

    }
  }
}
