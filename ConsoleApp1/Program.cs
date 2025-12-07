using System.Runtime.CompilerServices;

public class Extensions
{
    Dictionary<string, string> Extension = new Dictionary<string, string>()
    {
        { ".mp3", "MPEG3-Audio File" },
        { ".mp4", "MPEG3 - Video file" },
        { ".omv", "OMNeT++ Model/Simulation File" },
        { ".pdf", "Portable document Format" },
        { ".doc", "Microsoft Word Document" },
        { ".docx", "Microsoft Word Open XML Document" },
        { ".xls", "Microsoft Excel Spreadsheet" },
        { ".xlsx", "Microsoft Excel Open XML Spreadsheet" },
        { ".txt", "Text File" },
        { ".png", "Portable Network Graphics" },
        { ".ipg", "iPod Game File (Apple)" },
        { ".jpeg", "Joint Photographic Experts Group" },
        { ".gif", "Graphics Interchange Format" },
        { ".bmp", "Bitmap Image File" },
        { ".zip", "Zipped Archive File" },
        { ".rar", "RAR Archive File" },
        { ".exe", "Windows Executable File" },
        { ".dll", "Dynamic Link Library" },
        { ".html", "HyperText Markup Language File" },
        { ".css", "Cascading Style Sheets File" },
        { ".js", "JavaScript File" },
        { ".json", "JavaScript Object Notation File" },
        { ".xml", "eXtensible Markup Language File" },
        { ".csv", "Comma-Separated Values File" },
        { ".ppt", "Microsoft PowerPoint Presentation" },
        { ".pptx", "Microsoft PowerPoint Open XML Presentation" },
        { ".mov", "Apple QuickTime Movie File" },
        {".avi", "Audio Video Interleave File" },
        {".mkv", "Matroska Video File" },
        {".webm", "WebM Video File" }
    };
    public void ShowFileType(String fileExtension)
    {
        if (Extension.TryGetValue(fileExtension, out string Description))
        {
            Console.WriteLine($" '{fileExtension}' is: {Description}");
        }
        else
        {
            Console.WriteLine($"File extension '{fileExtension}' is not recognized.");
        }
    }


}
