$( document ).ready(function() {
    console.log("Tableau get ready")

    initViz()

})

function initViz() {

    // https://10ay.online.tableau.com/api/3.4/sites/site-id/projects/project-id
    // server connection

    let attributes = "https://10ay.online.tableau.com/t/heartdiseasepollytam/views/graphs2/Sheet1?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link"

    var containerDiv = document.getElementById("attributes"),
    url = attributes
    var viz = new tableau.Viz(containerDiv, url);

    let resultbyAge = "https://10ay.online.tableau.com/t/heartdiseasepollytam/views/graphs/byAgeGroup?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link"

    var containerDiv = document.getElementById("resultbyAge"),
    url = resultbyAge
    var viz = new tableau.Viz(containerDiv, url);

    let avgHeartrate = "https://10ay.online.tableau.com/t/heartdiseasepollytam/views/graphs/AvgHeartratebyAge_Sex?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link"

    var containerDiv = document.getElementById("avgHeartrate"),
    url = avgHeartrate
    var viz = new tableau.Viz(containerDiv, url);

    let avgMajorvessels = "https://10ay.online.tableau.com/t/heartdiseasepollytam/views/graphs/numberofmajorvessels0-3coloredbyflourosopy?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link"

    var containerDiv = document.getElementById("avgMajorvessels"),
    url = avgMajorvessels
    var viz = new tableau.Viz(containerDiv, url);

    let avgChestpain = "https://10ay.online.tableau.com/t/heartdiseasepollytam/views/graphs/chestpaintype?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link"

    var containerDiv = document.getElementById("avgChestpain"),
    url = avgChestpain
    var viz = new tableau.Viz(containerDiv, url);
}