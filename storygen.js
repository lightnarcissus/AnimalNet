
<!-- TWO STEPS TO INSTALL STORY GENERATOR:



  1.  Copy the coding into the HEAD of your HTML document

  2.  Add the last code into the BODY of your HTML document  -->



<!-- STEP ONE: Paste this code into the HEAD of your HTML document  -->



<HEAD>



<!-- This script and many more are available free online at -->

<!-- The JavaScript Source!! http://www.javascriptsource.com -->

<!-- Original:  Ben Joffe () -->

<!-- Web Site:  http://www.joffe.tk/ -->



</HEAD>



<!-- STEP TWO: Copy this code into the BODY of your HTML document  -->



<BODY>



<!-- This script and many more are available free online at -->

<!-- The JavaScript Source!! http://www.javascriptsource.com -->

<!-- Original:  Ben Joffe -->

<!-- Web Site:  http://www.joffe.tk/ -->

<SCRIPT LANGUAGE="JavaScript">

function storytest() {

if (character.value=='') alert("Please enter the name of your character");

if (character.value!='') story(character.value,sex.options.selectedIndex);

}

function story(char,charsex) {

var his="his"

var him="him"

var he="he"

var girl="girl"

var son="son";

if (charsex=="1") {

son="daughter";

his="her";

he="she";

girl="guy";

him="her";

}

var index;

var tmpStr;

var tmpChar;

var preString;

var postString;

var strlen;

tmpStr = char.toLowerCase();

strLen = tmpStr.length;

if (strLen > 0)  {

for (index = 0; index < strLen; index++)  {

if (index == 0)  {

tmpChar = tmpStr.substring(0,1).toUpperCase();

postString = tmpStr.substring(1,strLen);

tmpStr = tmpChar + postString;

}else{

tmpChar = tmpStr.substring(index, index+1);

if (tmpChar == " " && index < (strLen-1))  {

tmpChar = tmpStr.substring(index+1, index+2).toUpperCase();

preString = tmpStr.substring(0, index+1);

postString = tmpStr.substring(index+2,strLen);

tmpStr = preString + tmpChar + postString;

}}}

char=tmpStr;

heading.innerHTML="<b><big>The Story Of "+char+"</big></b>";



var country=Math.round(Math.random()*20);

var country2=Math.round(Math.random()*20);

var countryarray=new Array("South Africa","China","Bali","Canada","Brazil","France","Italy","Germany","Russia","Tokalue","Scotland","England","Ireland","Greenland","Iceland","Israel","Japan","Peru","Egypt","Mexico","Java","Scandinavia");



var burns=Math.round(Math.random()*2);

var burnarray=new Array("1st","2nd","3rd");



var cost=Math.round(Math.random()*5);

var costarray=new Array("$10 000","$45 000","$120 000","$3","$750 000");



var years=Math.round(Math.random()*44)+3;



var part0=Math.round(Math.random()*9)

var part1=Math.round(Math.random()*12)

var part2=Math.round(Math.random()*12)

var part3=Math.round(Math.random()*9)

var part4=Math.round(Math.random()*9)

var part5=Math.round(Math.random()*9)

var part6=Math.round(Math.random()*11)

var part7=Math.round(Math.random()*9)

var part8=Math.round(Math.random()*9)

var part9=Math.round(Math.random()*9)



var part0array=new Array(" slept in all day with"," was owed money by"," fought "+his+" enemy:"," traveled with"," saw a movie made by"," got a letter bomb from"," discovered"," went swimming with"," was friends with"," almost got killed by");

var part1array=new Array(" the T800"," Homer Simpson"," "+his+" mum"," a baby boy"," an axe murderer"," a wild dog"," a man in a wheelchair"," Fat Bastard"," a sexy model"," Ben Joffe"," Karl's mum"," Mr Harnwell"," John Howard");

var part2array=new Array(" under the bed"," on an ironing board"," in the fire place"," in "+countryarray[country]," in "+countryarray[country]," in "+countryarray[country]," after leaping from a crashing plane"," after winning the lottery"," in an icy cave"," on a passenger jet"," on a pirate ship"," down the back of Galston High");

var part3array=new Array(" during an important business meeting"," and got "+burnarray[burns]+" degree burns"," and fell into the eternal pit of hell"," and got banished from the country"," and almost got killed by an army of birds"," and got locked in prison"," during a hail storm"," and went around killing rats with a jackhammer"," during the third world war"," and got locked in a room full of greasy meat");

var part4array=new Array(" because "+he+" had no sleep the night before"," for no reason at all"," because "+he+" felt like it"," very happily"," in a sad mood"," because "+his+" leg hurt"," because "+his+" leg hurt"," but it was all an accident"," feeling very foolish"," on purpose"," then stormed out");

var part5array=new Array(" and snapped "+his+" ankle"," and all hell broke loose"," and a heated argument arose"," and went for a long walk through the park"," and banged "+his+" head on a wall"," and decided to sleep it off"," and everyone felt very sympathetic"," and fell violently ill"," and chased a bunny"," and went on a rampage");

var part6array=new Array(" which caused public outcry"," which completely freaked "+him+" out","which got "+him+" in a lot of trouble,"," which made "+him+" cry,"," which caused an avalanche,"," so everyone bowed down to "+char+","," which upset everybody,"," which started a party,",". "+char+" just dodged three bullets,",". Then "+char+" ran around like a lunatic,",". "+char+" then escaped through a secret passage,",", "+char+" then met "+his+" long lost "+son+": "+char+" the second,");

var part7array=new Array(" "+he+" grabbed the detonator"," "+he+" stole a car"," "+he+" blew up a truck with a hand grenade"," "+he+" felt a sudden ray of hope"," "+he+" made a run for it"," "+he+" jumped out of the way as the roof collapsed"," "+he+" went around killing rats with plastic bombs"," "+he+" shot all the bad guys"," "+he+" made a giant leap across the ravine"," "+he+" called the police");

var part8array=new Array(" and which defies what that dam fortune teller told "+him+","," and as if it were a miracle"," and to the disappointment of some"," and while wearing "+his+" lucky backpack"," and with relative ease"," and just as "+he+" hoped"," and to the surprise of the audience"," and as "+he+" nearly gave up all hope"," and with the help of "+costarray[cost]+" worth of special effects"," and with "+his+" last ounce of strength");

var part9array=new Array(" "+he+" got promoted to field marshal."," "+he+" killed the bad guy and made it away with minimal injuries."," "+he+" got kidnapped and tortured to death."," "+he+" got caught by the police and was sentenced to "+years+" years in prison."," "+he+" got the money and lived the rest of "+his+" life in "+countryarray[country2]," "+he+" failed the mission and the bad guys made it away with the gold."," "+he+" accidently tripped and smashed "+his+" face against a rock."," "+he+" defeated "+his+" enemy and the world was safe again... but for how long?"," "+he+" escaped narrowly and hitch-hiked all the way home."," "+he+" got the "+girl+", the treasure and a nasty rash."," "+he+" got the "+girl+", the treasure and a nasty rash.");



storyarea.innerHTML=char+part0array[part0]+part1array[part1]+part2array[part2]+part3array[part3]+part4array[part4]+part5array[part5]+part6array[part6]+part7array[part7]+part8array[part8]+part9array[part9];

}

}

</script>



<table border="0" cellpadding="5" cellspacing="0" class="main" width="250">

  <tr>

    <td align="center" colspan="2"><div id=heading><b><big>Ben Joffe's </big><big>Story Generator</big></b></div>

    <textarea id=storyarea rows="8" cols="40" readonly onfocus=this.blur() class="form" style="padding: 5">Please enter your name and select your sex to have a random story about you generated. There are over 1 billion different possible stories so have fun! This was created by Benjamin M. Joffe.</textarea></td>

  </tr>

  <tr>

    <td align="right">Name</td>

    <td><input type="text" name=character maxlength=15 size="20" class="form"></td>

  </tr>

  <tr>

    <td align="right">Sex:</td>

    <td><select name="sex" size="1" class="form"><option>Male</option><option>Female</option></select></td>

  </tr>

  <tr>

    <td align="center"></td>

    <td><input type="button" onclick=storytest() value="Generate Story" class="form"></td>

  </tr>

</table>



<p><center>

<font face="arial, helvetica" size"-2">Free JavaScripts provided<br>

by <a href="http://javascriptsource.com">The JavaScript Source</a></font>

</center><p>



<!-- Script Size:  8.26 KB -->