% import model
<!DOCTYPE html>

<html>
<head>
    <meta charset="UTF-8">
</head>

<body>

  <h1>Vislice</h1>
  <h2>Igraš igro</h2>
  <h3>Si v stanju {{ stanje }}</h3>

  <h4>{{igra.pravilni_del_gesla()}}</h4>

  <h3>Nepravilni ugibi</h3>
  <h4>{{ igra.nepravilni_ugibi() }}</h4>

  <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">

% if stanje == model.ZMAGA:

  <h1>ZMAGA</h1>
  <h3>Bravo, zmagal si</h3> 
  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% elif stanje == model.PORAZ:

  <h1>PORAZ</h1>
  <h3>Ojoj, izgubil si</h3>
  <p>Pravilno geslo: <b>{{igra.geslo}}</b></p>
  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% else:

  <form action="/igra/{{ id_igre }}/" method="post">
    Črka: <input type="text" name="crka" />
    <button type="submit">Ugibaj</button>
  </form>

% end

</body>

</html>