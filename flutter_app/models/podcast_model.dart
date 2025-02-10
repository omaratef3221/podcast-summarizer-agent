class Podcast {
  String title;
  String link;
  String summary;

  Podcast({this.title = '', this.link = '', this.summary = ''});

  factory Podcast.fromJson(Map<String, dynamic> json) {
    return Podcast(
      title: json['title'],
      link: json['link'],
      summary: json['summary'],
    );
  }
}