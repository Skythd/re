//C#
using System;
using Assistant;
using System.Collections.Generic;
namespace RazorEnhanced
{
    public class Script
    {
		public Script()
		{
			Misc.SendMessage("Constructor");
		}

        public void Run()
        {
			Misc.SendMessage("Run");
        }
    }
}