import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:flutter/gestures.dart';

class AboutMe extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        children: [
          SizedBox(
            height: 20,
          ),
          Text(
            'About Me',
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
            ),
          ),
          SizedBox(height: 16),
          RichText(
            text: TextSpan(
              style: DefaultTextStyle.of(context).style,
              children: <TextSpan>[
                TextSpan(
                  text: 'API REQUEST AVEC ABOUT ME',
                  style: TextStyle(
                    color: Colors.black, // Couleur du texte
                    fontSize: 16, // Taille de police
                  ),
                ),
                TextSpan(
                  text: '\n\nMes compétences :',
                  style: TextStyle(
                    color: Colors.blue, // Couleur du texte
                    fontSize: 18, // Taille de police
                    fontWeight: FontWeight.bold, // Gras
                  ),
                ),
                TextSpan(
                  text: '\n• Flutter',
                  style: TextStyle(
                    fontSize: 16,
                  ),
                ),
                TextSpan(
                  text: '\n• Dart',
                  style: TextStyle(
                    fontSize: 16, // Taille de police
                  ),
                ),
                TextSpan(
                  text: '\n• Mobile App Development',
                  style: TextStyle(
                    fontSize: 16, // Taille de police
                  ),
                ),
                TextSpan(
                  text:
                      '\n\nPour plus d\'informations, contactez moi sur LinkedIn : ',
                  style: TextStyle(
                    color: Colors.blue, // Couleur du texte
                    fontSize: 16, // Taille de police
                  ),
                ),
                TextSpan(
                  text: 'https://www.linkedin.com/in/eliot-praz/',
                  style: TextStyle(
                    color: Colors.blue, // Couleur du texte
                    fontSize: 16, // Taille de police
                    decoration: TextDecoration.underline, // Souligner
                  ),
                  recognizer: TapGestureRecognizer()
                    ..onTap = () async {
                      // Ouvrir un navigateur web lorsque le lien est tapé
                      const url = 'https://www.linkedin.com/in/eliot-praz/';
                      if (await canLaunch(url)) {
                        await launch(url);
                      } else {
                        throw 'Impossible d\'ouvrir le lien $url';
                      }
                    },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
