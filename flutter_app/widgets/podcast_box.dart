import 'package:flutter/material.dart';

class PodcastBox extends StatelessWidget {
  final String title;
  final String link;
  final String summary;

  PodcastBox({required this.title, required this.link, required this.summary});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(16),
      margin: EdgeInsets.all(16),
      decoration: BoxDecoration(
        border: Border.all(color: Colors.blue),
        borderRadius: BorderRadius.circular(8),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('Latest Title', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          SizedBox(height: 8),
          Text('Title: $title'),
          Text('Link: $link'),
          Text('Summary: $summary'),
        ],
      ),
    );
  }
}