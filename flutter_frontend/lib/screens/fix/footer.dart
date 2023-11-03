import 'package:flutter/material.dart';

//Fix footer
class Footer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 75,
      color: Colors.blue,
      child: Center(
        child: Text('Pied de page'),
      ),
    );
  }
}
