using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace SeleniumTestOpenChrome
{
    class Program
    {
        static void Main(string[] args)
        {
            //initializing the Chrome Driver
            var chrome = new ChromeDriver();
            //go to Google
            chrome.Navigate().GoToUrl("http://google.com");

            //find the serach bar by name
            chrome.FindElementByName("q").SendKeys("Selenium");
            //search for Selenium
            IWebElement div = chrome.FindElement(By.ClassName("jsb"));
            //search for the button and then click it
            IWebElement searchButton = chrome.FindElement(By.Name("btnK"));
            searchButton.Click();

            //search for Selenium field
            IWebElement seleniumWebsite = chrome.FindElement(By.ClassName("_Rm"));

            //checking is there an Selenium field
            if (seleniumWebsite.Displayed)
            {
                IJavaScriptExecutor js = chrome as IJavaScriptExecutor;
                js.ExecuteScript("alert('Yes, there is an www.seleniumhq.org in this page');");
                System.Threading.Thread.Sleep(8000);
                IAlert alert = chrome.SwitchTo().Alert();
                alert.Accept();
                Console.Read();
            }
            else
            {
                IJavaScriptExecutor js = chrome as IJavaScriptExecutor;
                js.ExecuteScript("alert('Sorry, there is not a www.seleniumhq.org in this page');");
                System.Threading.Thread.Sleep(8000);
                IAlert alert = chrome.SwitchTo().Alert();
                alert.Accept();
                Console.Read();
            }
            //close the browser
            chrome.Quit();      
        }
    }
}
