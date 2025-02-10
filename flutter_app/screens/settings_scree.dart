import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/api_service.dart';

class SettingsScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Settings'),
      ),
      body: ListView(
        children: [
          ListTile(
            title: Text('Hit and Check Latest'),
            onTap: () {
              Provider.of<ApiService>(context, listen: false).hitApi();
            },
          ),
          ListTile(
            title: Text('Schedule'),
            onTap: () {
              // Implement scheduling logic here
            },
          ),
        ],
      ),
    );
  }
}