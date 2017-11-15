<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default_WAR.aspx.cs" Inherits="MegaChallengeWar.Default_WAR" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Button ID="PlayButton" runat="server" OnClick="PlayButton_Click" Text="Play War!" />
            <br />
            <br />
            <asp:Label ID="resultLabel" runat="server"></asp:Label>
        </div>
    </form>
</body>
</html>
