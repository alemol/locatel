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
    "presunto_motivo": "BACHEO",
    "texto": "Solicito que reparen los baches enormes que hay en el asfalto.",
    "valores_confianza": [
        {
            "confianza": "4.056988522904703e-09",
            "motivo": "ALARMAS VECINALES"
        },
        {
            "confianza": "3.261275196564384e-05",
            "motivo": "ALERTA SISMICA / FALLA DE ALTAVOZ"
        },
        {
            "confianza": "0.00011930931941606104",
            "motivo": "ALUMBRADO"
        },
        {
            "confianza": "1.767668322827376e-08",
            "motivo": "APOYO SERVICIOS FUNERARIOS"
        },
        {
            "confianza": "6.671320162965344e-10",
            "motivo": "ASESORÍA DE TERCEROS ACREDITADOS"
        },
        {
            "confianza": "1.3292391543018311e-07",
            "motivo": "ASESORÍA JURÍDICA"
        },
        {
            "confianza": "4.7037343620104366e-07",
            "motivo": "ASISTENCIA SOCIAL"
        },
        {
            "confianza": "4.573704526222855e-09",
            "motivo": "ASISTENCIA VETERINARIA"
        },
        {
            "confianza": "0.9976219534873962",
            "motivo": "BACHEO"
        },
        {
            "confianza": "6.5154376898135524e-06",
            "motivo": "BALIZAMIENTO"
        },
        {
            "confianza": "8.794775112619391e-07",
            "motivo": "BARBECHO / CHAPONEO"
        },
        {
            "confianza": "1.5413505138894834e-07",
            "motivo": "BECAS"
        },
        {
            "confianza": "2.979243618028704e-06",
            "motivo": "CONSTRUCCION DE RAMPAS"
        },
        {
            "confianza": "4.331582592609351e-10",
            "motivo": "CONTANCIA DE PRODUCTOR AGROPECUARIO"
        },
        {
            "confianza": "2.0188119833619567e-06",
            "motivo": "COVID"
        },
        {
            "confianza": "7.834269695194962e-07",
            "motivo": "COVID-GENERALES"
        },
        {
            "confianza": "4.4450111147398275e-08",
            "motivo": "COVID-LABORAL"
        },
        {
            "confianza": "4.58285376225831e-06",
            "motivo": "COVID-MEDIDAS SANITARIAS"
        },
        {
            "confianza": "6.6130714237999655e-09",
            "motivo": "COVID-REAPERTURA"
        },
        {
            "confianza": "1.1101877195329735e-09",
            "motivo": "CRÉDITO DE VIVIENDA"
        },
        {
            "confianza": "8.61082153278403e-05",
            "motivo": "DESAZOLVE"
        },
        {
            "confianza": "3.7423309549922124e-05",
            "motivo": "FALTA DE AGUA"
        },
        {
            "confianza": "7.594125781906769e-05",
            "motivo": "FUGA DE AGUA"
        },
        {
            "confianza": "4.643484032840206e-07",
            "motivo": "LIMPIEZA VIA PUBLICA"
        },
        {
            "confianza": "9.396184275090036e-09",
            "motivo": "LLAVE CDMX"
        },
        {
            "confianza": "0.0009946560021489859",
            "motivo": "MANTENIMIENTO DE COLADERA / ALCANTARILLA"
        },
        {
            "confianza": "8.028893353184685e-05",
            "motivo": "MANTENIMIENTO DE POSTE"
        },
        {
            "confianza": "6.228509846550878e-06",
            "motivo": "MANTENIMIENTO DRENAJE"
        },
        {
            "confianza": "4.679141056840308e-05",
            "motivo": "MANTENIMIENTO PARQUE / AREA VERDE"
        },
        {
            "confianza": "4.769008228322491e-05",
            "motivo": "MANTENIMIENTO SEMÁFOROS"
        },
        {
            "confianza": "1.8797603843268007e-05",
            "motivo": "MANTENIMIENTO VÍA PÚBLICA"
        },
        {
            "confianza": "1.4070009157762797e-08",
            "motivo": "PADRÓN DE ARTESANAS SEPI"
        },
        {
            "confianza": "5.826684719067998e-05",
            "motivo": "PAVIMENTACION"
        },
        {
            "confianza": "3.567042439200918e-09",
            "motivo": "PENSIÓN DE ADULTOS MAYORES"
        },
        {
            "confianza": "0.0001657303946558386",
            "motivo": "PODA / RETIRO ARBOL"
        },
        {
            "confianza": "6.302379729206109e-10",
            "motivo": "PROGRAMA APOYO A CUIDADORES"
        },
        {
            "confianza": "3.302261757198721e-05",
            "motivo": "PROTECCION CIVIL"
        },
        {
            "confianza": "5.767625680164201e-06",
            "motivo": "QUEJA DE TRANSPORTE PUBLICO"
        },
        {
            "confianza": "4.451259883353487e-06",
            "motivo": "QUEJA FUNCIONARIO"
        },
        {
            "confianza": "4.692274160333909e-05",
            "motivo": "RECOLECCIÓN BASURA"
        },
        {
            "confianza": "1.685450712329839e-08",
            "motivo": "REGISTRO FERIAS INDIGENAS"
        },
        {
            "confianza": "7.045805432426278e-07",
            "motivo": "REINSCRIPCION AL CENDI"
        },
        {
            "confianza": "2.5874342099996284e-06",
            "motivo": "REPARACION DE EMPEDRADO"
        },
        {
            "confianza": "2.1473729461263247e-08",
            "motivo": "RETIRO AMBULANTE"
        },
        {
            "confianza": "1.3912026588513982e-05",
            "motivo": "RETIRO CASCAJO, ESCOMBRO, AZOLVE, RAMAS"
        },
        {
            "confianza": "4.325304416852305e-06",
            "motivo": "SOLICITU DE AUDIENCIA"
        },
        {
            "confianza": "5.924847457094984e-08",
            "motivo": "SOLICITUD DE CONCERTACIÓN VECINAL"
        },
        {
            "confianza": "0.0003978286113124341",
            "motivo": "SOLICITUD DE VIGILANCIA"
        },
        {
            "confianza": "8.257480033080355e-08",
            "motivo": "SOLICITUD DE VOLANTEO"
        },
        {
            "confianza": "1.939996385758036e-09",
            "motivo": "SOLICITUD ESTUDIO SOCIOECONOMICO"
        },
        {
            "confianza": "1.3597634129780545e-09",
            "motivo": "SOLICITUD EVALUACIÓN DE RIESGO"
        },
        {
            "confianza": "1.5661160432500765e-05",
            "motivo": "SOLICITUD/SEGURO DE DESEMPLEO"
        },
        {
            "confianza": "2.7659673662583373e-08",
            "motivo": "TRAMITES / INFO VEHICULAR"
        },
        {
            "confianza": "2.8232368549652165e-06",
            "motivo": "TRAMITES E INFORMACION"
        },
        {
            "confianza": "1.008707783967111e-08",
            "motivo": "TRAMITES/INFO VEHICULAR"
        },
        {
            "confianza": "1.1595670912356582e-06",
            "motivo": "USO DE SUELO"
        },
        {
            "confianza": "3.4869517548941076e-05",
            "motivo": "VEHÍCULO ABANDONADO / CHATARRIZACIÓN"
        },
        {
            "confianza": "1.734049874357879e-05",
            "motivo": "VENTA DE ALCOHOL / DROGA"
        },
        {
            "confianza": "7.589734650537139e-06",
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
