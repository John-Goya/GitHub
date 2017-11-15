using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ChallengeSimpleCalculator
{
    public partial class Default_010_Challenge : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void addButton_Click(object sender, EventArgs e)
        {
            
            int sumValue1 = int.Parse(this.inputValue1.Text);

            int sumValue2 = int.Parse(this.inputValue2.Text);

            int resultValue = sumValue1 + sumValue2;

            resultValueLabel.Text = resultValue.ToString();
        }

        protected void subtractButtonClick(object sender, EventArgs e)
        {
            int differenceValue1 = int.Parse(this.inputValue1.Text);

            int differenceValue2 = int.Parse(this.inputValue2.Text);

            int resultValue = differenceValue1 - differenceValue2;

            resultValueLabel.Text = resultValue.ToString();
        }

        protected void multiplyButtonClick(object sender, EventArgs e)
        {
            int productValue1 = int.Parse(this.inputValue1.Text);

            int productValue2 = int.Parse(this.inputValue2.Text);

            int resultValue = productValue1 * productValue2;

            resultValueLabel.Text = resultValue.ToString();
        }

        protected void divideButtonClick(object sender, EventArgs e)
        {
            double quotientValue1 = double.Parse(this.inputValue1.Text);

            double quotientValue2 = double.Parse(this.inputValue2.Text);

            double resultValue = quotientValue1 / quotientValue2;

            resultValueLabel.Text = resultValue.ToString();
        }
    }
}