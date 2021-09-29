# locatel

Clasificación automática de solicitudes de atención ciudadana para la CDMX.


La base de datos del SUAC (sistema unificado de atención ciudadana) de la CDMX, contiene un campo con las solicitudes de atención en modo texto libre (formato no estructurado), por ejemplo '_Solicito se pode la raíz de un árbol que está levantando la banqueta de la calle_'; así como un campo con las coordenadas. Actualmente esta información es evaluada manualmente para determinar que se trata de una solicitud de tipo **PODA** y que correspondería a la **Alcaldía Venustiano Carranza atenderla**.

El servicio web implementado en este repositorio permite asistir la clasificación automática de solicitudes, mediante técnicas de aprendizaje profundo y procesamiento de lenguaje natural, con la intención de hacer más eficiente el procesamiento de la información de los ciudadanos. 

## Dependencias

Python 3.8.0 y lo indicado en el archivo de requerimientos

`pip install -r requirements.txt`

## Ejecución del servicio

`python wsgi.py`

## Verificación de servicio funcionando:

``` 
* Serving Flask app "application" (lazy loading) 
  * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
```

En entorno local (server), hacer el envío por HTTP al puerto 5000 [http://localhost:5000](http://localhost:5000). En producción, es necesario configurar el host y los puertos necesarios.

## Envío de peticiones

Las peticiones deben hacerse con HTTP POST usando el header "Content-Type: application/json" mediante un JSON codificado en UTF-8 con campo **"texto"** conteniendo la descripción de la solicitud. Por ejemplo:

``` 
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"texto":"Solicito que reparen los baches enormes que hay en el asfalto."}' \
     http://localhost:5000/locatel
```


## Recepción de Respuesta del servicio

La clasificación de reportes de atención ciudadana para la ciudad de México está basada en _deep learning_, por ello en la respuesta se presentan valores numéricos correspondientes al score de **"confianza"** que se puede tener en la asociación entre una solicitud y un motivo asociado de manera automática. El score de confianza es un número real en el intervalo `[0.0, 1.0]` tal que los valores bajos (cercanos a cero) corresponden a baja confianza mientras que los valores altos (cercanos a uno), corresponden a alta confianza. Por ejemplo:


```
{
    "confianza": "0.9999691247940063",
    "presunto_motivo": "BACHEO",
    "texto": "Solicito que reparen los baches enormes que hay en el asfalto.",
    "valores_confianza": [
        {
            "confianza": "5.855997464720986e-09",
            "motivo": "ALARMAS VECINALES"
        },
        {
            "confianza": "1.6508097999690108e-08",
            "motivo": "ALERTA SISMICA"
        },
        {
            "confianza": "9.376478971034885e-08",
            "motivo": "ALUMBRADO"
        },
        {
            "confianza": "2.1950118167524124e-08",
            "motivo": "APOYO SERVICIOS FUNERARIOS"
        },
        {
            "confianza": "2.013153910240817e-08",
            "motivo": "ASESORÍA DE TERCEROS ACREDITADOS"
        },
        {
            "confianza": "6.779178875149228e-06",
            "motivo": "ASESORÍA JURÍDICA"
        },
        {
            "confianza": "2.101147172917095e-10",
            "motivo": "ASISTENCIA SOCIAL"
        },
        {
            "confianza": "3.2906490332607063e-07",
            "motivo": "ASISTENCIA VETERINARIA"
        },
        {
            "confianza": "0.9999691247940063",
            "motivo": "BACHEO"
        },
        {
            "confianza": "2.1420747398082085e-09",
            "motivo": "BALIZAMIENTO"
        },
        {
            "confianza": "1.1015010414894277e-07",
            "motivo": "BARBECHO / CHAPONEO"
        },
        {
            "confianza": "2.793836095804636e-08",
            "motivo": "BECAS"
        },
        {
            "confianza": "2.995577233377844e-06",
            "motivo": "COVID"
        },
        {
            "confianza": "2.150648192866811e-08",
            "motivo": "CRÉDITO DE VIVIENDA"
        },
        {
            "confianza": "1.0316749694538885e-06",
            "motivo": "DESAZOLVE"
        },
        {
            "confianza": "3.2258881788038707e-07",
            "motivo": "FALTA DE AGUA"
        },
        {
            "confianza": "4.6606808723481663e-07",
            "motivo": "FUGA DE AGUA"
        },
        {
            "confianza": "1.660583670570759e-08",
            "motivo": "LIMPIEZA VIA PUBLICA"
        },
        {
            "confianza": "1.7826150278121844e-10",
            "motivo": "LLAVE CDMX"
        },
        {
            "confianza": "7.1920558184501715e-06",
            "motivo": "MANTENIMIENTO DE COLADERA / ALCANTARILLA"
        },
        {
            "confianza": "8.446786523563787e-07",
            "motivo": "MANTENIMIENTO DRENAJE"
        },
        {
            "confianza": "1.0973845832040752e-07",
            "motivo": "MANTENIMIENTO PARQUE / AREA VERDE"
        },
        {
            "confianza": "5.1427299752049294e-08",
            "motivo": "MANTENIMIENTO SEMÁFOROS"
        },
        {
            "confianza": "1.0201487157246447e-06",
            "motivo": "MANTENIMIENTO VÍA PÚBLICA"
        },
        {
            "confianza": "2.041733068836038e-06",
            "motivo": "PAVIMENTACION"
        },
        {
            "confianza": "5.0249401084556666e-08",
            "motivo": "PODA / RETIRO ARBOL"
        },
        {
            "confianza": "2.941054344507421e-10",
            "motivo": "PROGRAMA APOYO A CUIDADORES"
        },
        {
            "confianza": "4.5485478494811105e-08",
            "motivo": "PROTECCION CIVIL"
        },
        {
            "confianza": "7.931525658477767e-09",
            "motivo": "QUEJA DE TRANSPORTE PUBLICO"
        },
        {
            "confianza": "1.642347369212871e-10",
            "motivo": "QUEJA FUNCIONARIO"
        },
        {
            "confianza": "2.1485819345912205e-08",
            "motivo": "RECOLECCIÓN BASURA"
        },
        {
            "confianza": "1.130492410794659e-08",
            "motivo": "REGISTRO FERIAS INDIGENAS"
        },
        {
            "confianza": "6.668334329162917e-09",
            "motivo": "REINSCRIPCION AL CENDI"
        },
        {
            "confianza": "2.4702144401089754e-06",
            "motivo": "REPARACION DE EMPEDRADO"
        },
        {
            "confianza": "2.659982234476388e-10",
            "motivo": "RETIRO AMBULANTE"
        },
        {
            "confianza": "3.527275111991912e-07",
            "motivo": "RETIRO CASCAJO, ESCOMBRO, AZOLVE, RAMAS"
        },
        {
            "confianza": "8.449433863688682e-08",
            "motivo": "SOLICITU DE AUDIENCIA"
        },
        {
            "confianza": "4.377609386096992e-08",
            "motivo": "SOLICITUD DE CONCERTACIÓN VECINAL"
        },
        {
            "confianza": "8.542100999875402e-07",
            "motivo": "SOLICITUD DE VIGILANCIA"
        },
        {
            "confianza": "5.465365120471688e-07",
            "motivo": "SOLICITUD DE VOLANTEO"
        },
        {
            "confianza": "3.797928638249459e-10",
            "motivo": "SOLICITUD ESTUDIO SOCIOECONOMICO"
        },
        {
            "confianza": "2.550905946918647e-06",
            "motivo": "SOLICITUD EVALUACIÓN DE RIESGO"
        },
        {
            "confianza": "9.564012914964337e-10",
            "motivo": "SOLICITUD/SEGURO DE DESEMPLEO"
        },
        {
            "confianza": "2.3735749477005186e-10",
            "motivo": "TRAMITES / INFO VEHICULAR"
        },
        {
            "confianza": "1.439288581650544e-07",
            "motivo": "USO DE SUELO"
        },
        {
            "confianza": "9.167552939004509e-09",
            "motivo": "VEHÍCULO ABANDONADO / CHATARRIZACIÓN"
        },
        {
            "confianza": "1.5218832061236753e-07",
            "motivo": "VENTA DE ALCOHOL / DROGA"
        },
        {
            "confianza": "5.460225338538294e-08",
            "motivo": "VERIFICACIÓN ADMINISTRATIVA"
        }
    ]
}
```



## Author

**Alejandro Molina-Villegas**

* [dblp](https://dblp.uni-trier.de/pers/hd/m/Molina=Villegas:Alejandro)
* [orcid](https://orcid.org/0000-0001-9398-8844)
* [CONACyT-CentroGeo](http://mid.geoint.mx/site/integrante/id/15.html)

<!-- * **Oscar Gerardo Sanchez Siordia** - [Conacyt-CentroGeo](http://mid.geoint.mx/site/integrante/id/31.html)
 -->

## Instituciones Participantes

  * [CentroGeo](https://www.centrogeo.org.mx/) - Centro de Investigación en Ciencias de Información Geoespacial
  * [GeoInt](http://www.geoint.mx/) - Laboratorio Nacional de Geointeligencia
  * [ADIP](https://adip.cdmx.gob.mx/) - Agencia Digital de Innovación Pública - CDMX
  * [CONACyT](http://www.conacyt.gob.mx/index.html) - Consejo Nacional de Ciencia y Tecnología


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
