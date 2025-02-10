import 'package:flutter/material.dart';
import 'package:mongo_dart/mongo_dart.dart';
import '../models/podcast_model.dart';

class MongoService with ChangeNotifier {
  Podcast _podcast = Podcast();
  bool _isLoading = false;

  Podcast get podcast => _podcast;
  bool get isLoading => _isLoading;

  Future<void> fetchLatestPodcast() async {
    _isLoading = true;
    notifyListeners();

    // Connect to MongoDB and fetch data
    final db = await Db.create('your_mongo_connection_string');
    await db.open();
    final collection = db.collection('podcasts');
    final latestPodcast = await collection.findOne(where.sortBy('releaseDate', descending: true));

    _podcast = Podcast.fromJson(latestPodcast);
    _isLoading = false;
    notifyListeners();
  }
}