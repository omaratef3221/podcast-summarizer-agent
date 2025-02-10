import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class ApiService with ChangeNotifier {
  Future<void> hitApi() async {
    final response = await http.get(
      Uri.parse('https://podcast-summarizer-agent.onrender.com/podcast_agent?flag=1'),
    );
    if (response.statusCode == 200) {
      // Handle success
    } else {
      // Handle error
    }
  }
}