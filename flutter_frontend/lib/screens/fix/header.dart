import 'package:flutter/material.dart';

class Header extends StatelessWidget implements PreferredSizeWidget {
  Size get preferredSize => Size.fromHeight(56.0);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: Colors.blue,
      title: Text('Mon Application'),
    );
  }
}
