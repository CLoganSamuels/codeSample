var magnitude = 1; //proportional to all weight and mole values
var mass_measured = false;
var all_measured = false;
var sig_digits = 5;
 
function createTable(){
    let row1 = "<tr><td><strong>Molecule</strong></td>";
    let row2 = "<tr><td><strong>Moles</strong></td>";
    let row3 = "<tr><td><strong>Grams</strong></td>";
    let i = 0;
    
    for (m of molecules){
        row1 += "<td>"+m.name+"</td>";
        row2 += box(i, "m");
        row3 += box(i, "g");
        i++;
    }   

    let table = "<table><tr>";
    table += row1 + "</tr>" + row2 + "</tr>" + row3;
    table += "</tr></table>";
    document.write(table);
    updateVals();
}

function box(i, unit){
    return("<td><input type=text id="+unit+i+" size=10 " +
    "onchange=changed(this)></td>");
}

function changed(c){
    let i = parseInt(c.id.substring(1));
    let v = parseFloat(c.value)/molecules[i].coeff;

    if (v){ //v must be a number
        mass_measured = c.id.charAt(0)==="g";
        if (mass_measured) v = massToMoles(v, molecules[i].weight);
        magnitude = v; 
    }
    updateVals();
}

function updateVals(){
    let moles, mass, m;
    for(n=0; n<molecules.length; n++){
        m = molecules[n];
        moles = magnitude * m.coeff;
        mass = molesToMass(moles, m.weight);

        document.getElementById("m"+n).value = sigFigs(moles, mass_measured);
        document.getElementById("g"+n).value = sigFigs(mass, true);   
    } 
}

function molesToMass(moles, molecular_weight){
        return(moles * molecular_weight);
}
function massToMoles(mass, molecular_weight){
        return(mass / molecular_weight);
}

function sigFigs(value, measured){
    if (measured || all_measured){
        return (value.toPrecision(sig_digits));
    }
    return (value.toString());
}

function update_sigs(newsigs){
    let v = parseInt(newsigs.value);

    if (v<3) sig_digits = 3;
    else if (v>10) sig_digits = 10;       
    else if (v) sig_digits = v; //if v is not NaN

    newsigs.value = sig_digits;
    updateVals();
}

function update_measured(){
    if (all_measured) all_measured = false;
    else all_measured = true;
    updateVals();
}

createTable();