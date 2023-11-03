import 'package:flutter/material.dart';
import 'package:flutter_frontend/screens/aboutme.dart';
import 'package:flutter_frontend/screens/blog.dart';
import 'package:flutter_frontend/screens/fix/footer.dart';
import 'package:flutter_frontend/screens/fix/header.dart';
import 'package:flutter_frontend/screens/home_content.dart';
import 'package:flutter_frontend/widgets/navbar.dart';

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int _currentIndex = 0;

  void _onItemTapped(int index) {
    setState(() {
      _currentIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: Header(),
      body: Column(
        children: <Widget>[
          Navbar(
            currentIndex: _currentIndex,
            onTap: _onItemTapped,
          ),
          Expanded(
            child: IndexedStack(
              index: _currentIndex,
              children: [
                HomeContent(),
                const Blog(),
                AboutMe(),
              ],
            ),
          ),
          Footer(),
        ],
      ),
    );
  }
}
