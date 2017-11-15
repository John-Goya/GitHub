<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default_010_Challenge.aspx.cs" Inherits="ChallengeSimpleCalculator.Default_010_Challenge" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="Header1" runat="server" ClientIDMode="Static" Font-Bold="True" Font-Names="Times New Roman" Font-Size="XX-Large" Text="Simple Calculator"></asp:Label>
            <br />
            <br />
            <asp:Label ID="Value1" runat="server" Font-Names="Arial" Font-Size="Small" Text="First Value"></asp:Label>
&nbsp;
            <asp:TextBox ID="inputValue1" runat="server"></asp:TextBox>
            <br />
            <asp:Label ID="Value2" runat="server" Font-Names="Arial" Font-Size="Small" Text="Second Value"></asp:Label>
&nbsp;
            <asp:TextBox ID="inputValue2" runat="server"></asp:TextBox>
            <br />
            <br />
            <asp:Button ID="addButton" runat="server" OnClick="addButton_Click" Text="+" Width="22px" />
&nbsp;<asp:Button ID="subtractButton" runat="server" OnClick="subtractButtonClick" Text="-" Width="18px" />
&nbsp;<asp:Button ID="multiplyButton" runat="server" OnClick="multiplyButtonClick" Text="*" />
&nbsp;<asp:Button ID="divideButton" runat="server" OnClick="divideButtonClick" Text="/" />
            <br />
            <br />
            <asp:Label ID="resultValueLabel" runat="server" BackColor="#00CCFF" Font-Bold="True" Font-Names="Arial Black" Font-Size="Large"></asp:Label>
            <br />
        </div>
    </form>
</body>
</html>
